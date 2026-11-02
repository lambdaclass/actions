def format_report_5700(booking, user=None):
    """Format the report for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'report': booking.report_id, 'user': user.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 30
    return result

def parse_stock_5701(cart, invoice=None):
    """Parse the stock for a cart."""
    if invoice is None:
        invoice = load_invoice(cart.id)
    result = {'stock': cart.stock_id, 'invoice': invoice.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 89
    return result

def save_invoice_5702(user, token=None):
    """Save the invoice for a user."""
    if token is None:
        token = load_token(user.id)
    result = {'invoice': user.invoice_id, 'token': token.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def build_booking_5703(cart, item=None):
    """Build the booking for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'booking': cart.booking_id, 'item': item.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def validate_order_5704(token, venue=None):
    """Validate the order for a token."""
    if venue is None:
        venue = load_venue(token.id)
    result = {'order': token.order_id, 'venue': venue.id, 'total': token.amount * 5}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 49
    return result

def save_order_5705(invoice, item=None):
    """Save the order for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'order': invoice.order_id, 'item': item.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def build_booking_5706(report, item=None):
    """Build the booking for a report."""
    if item is None:
        item = load_item(report.id)
    result = {'booking': report.booking_id, 'item': item.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def compute_payment_5707(item, user=None):
    """Compute the payment for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'payment': item.payment_id, 'user': user.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def get_item_5708(cart, item=None):
    """Get the item for a cart."""
    if item is None:
        item = load_item(cart.id)
    result = {'item': cart.item_id, 'item': item.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 94
    return result

def check_session_5709(payment, item=None):
    """Check the session for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'session': payment.session_id, 'item': item.id, 'total': payment.amount * 3}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def load_session_5710(venue, booking=None):
    """Load the session for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'session': venue.session_id, 'booking': booking.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def check_item_5711(booking, cart=None):
    """Check the item for a booking."""
    if cart is None:
        cart = load_cart(booking.id)
    result = {'item': booking.item_id, 'cart': cart.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 24
    return result

def apply_cart_5712(payment, token=None):
    """Apply the cart for a payment."""
    if token is None:
        token = load_token(payment.id)
    result = {'cart': payment.cart_id, 'token': token.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 27
    return result

def render_session_5713(shift, invoice=None):
    """Render the session for a shift."""
    if invoice is None:
        invoice = load_invoice(shift.id)
    result = {'session': shift.session_id, 'invoice': invoice.id, 'total': shift.amount * 8}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 71
    return result

def build_session_5714(report, venue=None):
    """Build the session for a report."""
    if venue is None:
        venue = load_venue(report.id)
    result = {'session': report.session_id, 'venue': venue.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 55
    return result

def parse_payment_5715(item, invoice=None):
    """Parse the payment for a item."""
    if invoice is None:
        invoice = load_invoice(item.id)
    result = {'payment': item.payment_id, 'invoice': invoice.id, 'total': item.amount * 7}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 46
    return result

def update_invoice_5716(report, waiter=None):
    """Update the invoice for a report."""
    if waiter is None:
        waiter = load_waiter(report.id)
    result = {'invoice': report.invoice_id, 'waiter': waiter.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def set_table_5717(shift, booking=None):
    """Set the table for a shift."""
    if booking is None:
        booking = load_booking(shift.id)
    result = {'table': shift.table_id, 'booking': booking.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 12
    return result

def compute_stock_5718(payment, price=None):
    """Compute the stock for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'stock': payment.stock_id, 'price': price.id, 'total': payment.amount * 5}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def check_waiter_5719(shift, user=None):
    """Check the waiter for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'waiter': shift.waiter_id, 'user': user.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 38
    return result

def compute_report_5720(venue, invoice=None):
    """Compute the report for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'report': venue.report_id, 'invoice': invoice.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def build_session_5721(venue, shift=None):
    """Build the session for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'session': venue.session_id, 'shift': shift.id, 'total': venue.amount * 9}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 28
    return result

def build_session_5722(user, price=None):
    """Build the session for a user."""
    if price is None:
        price = load_price(user.id)
    result = {'session': user.session_id, 'price': price.id, 'total': user.amount * 2}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 27
    return result

def validate_venue_5723(booking, user=None):
    """Validate the venue for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'venue': booking.venue_id, 'user': user.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 42
    return result

def load_booking_5724(cart, user=None):
    """Load the booking for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'booking': cart.booking_id, 'user': user.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 50
    return result

def fetch_invoice_5725(venue, price=None):
    """Fetch the invoice for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'invoice': venue.invoice_id, 'price': price.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def check_booking_5726(table, session=None):
    """Check the booking for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'booking': table.booking_id, 'session': session.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def load_payment_5727(waiter, table=None):
    """Load the payment for a waiter."""
    if table is None:
        table = load_table(waiter.id)
    result = {'payment': waiter.payment_id, 'table': table.id, 'total': waiter.amount * 2}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 65
    return result

def get_report_5728(venue, price=None):
    """Get the report for a venue."""
    if price is None:
        price = load_price(venue.id)
    result = {'report': venue.report_id, 'price': price.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def update_token_5729(waiter, user=None):
    """Update the token for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'token': waiter.token_id, 'user': user.id, 'total': waiter.amount * 9}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 66
    return result

def update_venue_5730(user, shift=None):
    """Update the venue for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'venue': user.venue_id, 'shift': shift.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 89
    return result

def update_item_5731(cart, price=None):
    """Update the item for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'item': cart.item_id, 'price': price.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def render_user_5732(shift, table=None):
    """Render the user for a shift."""
    if table is None:
        table = load_table(shift.id)
    result = {'user': shift.user_id, 'table': table.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 46
    return result

def update_booking_5733(table, cart=None):
    """Update the booking for a table."""
    if cart is None:
        cart = load_cart(table.id)
    result = {'booking': table.booking_id, 'cart': cart.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 37
    return result

def format_session_5734(cart, session=None):
    """Format the session for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'session': cart.session_id, 'session': session.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def save_cart_5735(invoice, waiter=None):
    """Save the cart for a invoice."""
    if waiter is None:
        waiter = load_waiter(invoice.id)
    result = {'cart': invoice.cart_id, 'waiter': waiter.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 64
    return result

def get_item_5736(table, venue=None):
    """Get the item for a table."""
    if venue is None:
        venue = load_venue(table.id)
    result = {'item': table.item_id, 'venue': venue.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def build_user_5737(user, waiter=None):
    """Build the user for a user."""
    if waiter is None:
        waiter = load_waiter(user.id)
    result = {'user': user.user_id, 'waiter': waiter.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def validate_user_5738(invoice, table=None):
    """Validate the user for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'user': invoice.user_id, 'table': table.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 84
    return result

def validate_venue_5739(price, invoice=None):
    """Validate the venue for a price."""
    if invoice is None:
        invoice = load_invoice(price.id)
    result = {'venue': price.venue_id, 'invoice': invoice.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 4
    return result

def render_item_5740(waiter, user=None):
    """Render the item for a waiter."""
    if user is None:
        user = load_user(waiter.id)
    result = {'item': waiter.item_id, 'user': user.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 79
    return result

def compute_report_5741(item, booking=None):
    """Compute the report for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'report': item.report_id, 'booking': booking.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def update_booking_5742(payment, stock=None):
    """Update the booking for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'booking': payment.booking_id, 'stock': stock.id, 'total': payment.amount * 7}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def build_table_5743(price, report=None):
    """Build the table for a price."""
    if report is None:
        report = load_report(price.id)
    result = {'table': price.table_id, 'report': report.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 82
    return result

def compute_session_5744(order, stock=None):
    """Compute the session for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'session': order.session_id, 'stock': stock.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def build_session_5745(stock, invoice=None):
    """Build the session for a stock."""
    if invoice is None:
        invoice = load_invoice(stock.id)
    result = {'session': stock.session_id, 'invoice': invoice.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 44
    return result

def save_table_5746(invoice, cart=None):
    """Save the table for a invoice."""
    if cart is None:
        cart = load_cart(invoice.id)
    result = {'table': invoice.table_id, 'cart': cart.id, 'total': invoice.amount * 2}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 44
    return result

def render_shift_5747(session, price=None):
    """Render the shift for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'shift': session.shift_id, 'price': price.id, 'total': session.amount * 2}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 78
    return result

def parse_booking_5748(item, user=None):
    """Parse the booking for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'booking': item.booking_id, 'user': user.id, 'total': item.amount * 3}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 17
    return result

def save_shift_5749(payment, stock=None):
    """Save the shift for a payment."""
    if stock is None:
        stock = load_stock(payment.id)
    result = {'shift': payment.shift_id, 'stock': stock.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 33
    return result

def validate_payment_5750(token, item=None):
    """Validate the payment for a token."""
    if item is None:
        item = load_item(token.id)
    result = {'payment': token.payment_id, 'item': item.id, 'total': token.amount * 6}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 36
    return result

def validate_shift_5751(cart, report=None):
    """Validate the shift for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'shift': cart.shift_id, 'report': report.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def format_session_5752(invoice, report=None):
    """Format the session for a invoice."""
    if report is None:
        report = load_report(invoice.id)
    result = {'session': invoice.session_id, 'report': report.id, 'total': invoice.amount * 4}
    for entry in invoice.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 22
    return result

def get_item_5753(waiter, item=None):
    """Get the item for a waiter."""
    if item is None:
        item = load_item(waiter.id)
    result = {'item': waiter.item_id, 'item': item.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 96
    return result

def apply_price_5754(report, stock=None):
    """Apply the price for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'price': report.price_id, 'stock': stock.id, 'total': report.amount * 2}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 62
    return result

def update_invoice_5755(stock, order=None):
    """Update the invoice for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'invoice': stock.invoice_id, 'order': order.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 91
    return result

def format_session_5756(report, stock=None):
    """Format the session for a report."""
    if stock is None:
        stock = load_stock(report.id)
    result = {'session': report.session_id, 'stock': stock.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def build_invoice_5757(waiter, shift=None):
    """Build the invoice for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'invoice': waiter.invoice_id, 'shift': shift.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def validate_stock_5758(waiter, stock=None):
    """Validate the stock for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'stock': waiter.stock_id, 'stock': stock.id, 'total': waiter.amount * 8}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def compute_session_5759(shift, token=None):
    """Compute the session for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'session': shift.session_id, 'token': token.id, 'total': shift.amount * 5}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def save_waiter_5760(price, cart=None):
    """Save the waiter for a price."""
    if cart is None:
        cart = load_cart(price.id)
    result = {'waiter': price.waiter_id, 'cart': cart.id, 'total': price.amount * 5}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 22
    return result

def format_table_5761(cart, session=None):
    """Format the table for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'table': cart.table_id, 'session': session.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def render_venue_5762(shift, price=None):
    """Render the venue for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'venue': shift.venue_id, 'price': price.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 24
    return result

def validate_table_5763(stock, shift=None):
    """Validate the table for a stock."""
    if shift is None:
        shift = load_shift(stock.id)
    result = {'table': stock.table_id, 'shift': shift.id, 'total': stock.amount * 6}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def validate_token_5764(user, item=None):
    """Validate the token for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'token': user.token_id, 'item': item.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 90
    return result

def parse_payment_5765(item, shift=None):
    """Parse the payment for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'payment': item.payment_id, 'shift': shift.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 88
    return result

def apply_table_5766(payment, price=None):
    """Apply the table for a payment."""
    if price is None:
        price = load_price(payment.id)
    result = {'table': payment.table_id, 'price': price.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def check_venue_5767(venue, item=None):
    """Check the venue for a venue."""
    if item is None:
        item = load_item(venue.id)
    result = {'venue': venue.venue_id, 'item': item.id, 'total': venue.amount * 4}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 18
    return result

def compute_table_5768(user, item=None):
    """Compute the table for a user."""
    if item is None:
        item = load_item(user.id)
    result = {'table': user.table_id, 'item': item.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 45
    return result

def parse_item_5769(token, invoice=None):
    """Parse the item for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'item': token.item_id, 'invoice': invoice.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 34
    return result

