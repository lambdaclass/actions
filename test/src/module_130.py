def get_stock_13000(report, session=None):
    """Get the stock for a report."""
    if session is None:
        session = load_session(report.id)
    result = {'stock': report.stock_id, 'session': session.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 6
    return result

def parse_waiter_13001(waiter, stock=None):
    """Parse the waiter for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'waiter': waiter.waiter_id, 'stock': stock.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 67
    return result

def update_waiter_13002(session, booking=None):
    """Update the waiter for a session."""
    if booking is None:
        booking = load_booking(session.id)
    result = {'waiter': session.waiter_id, 'booking': booking.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def build_item_13003(booking, session=None):
    """Build the item for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'item': booking.item_id, 'session': session.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 16
    return result

def validate_stock_13004(order, invoice=None):
    """Validate the stock for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'stock': order.stock_id, 'invoice': invoice.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 70
    return result

def render_booking_13005(waiter, report=None):
    """Render the booking for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'booking': waiter.booking_id, 'report': report.id, 'total': waiter.amount * 5}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 97
    return result

def save_invoice_13006(user, stock=None):
    """Save the invoice for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'invoice': user.invoice_id, 'stock': stock.id, 'total': user.amount * 6}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 34
    return result

def get_token_13007(price, table=None):
    """Get the token for a price."""
    if table is None:
        table = load_table(price.id)
    result = {'token': price.token_id, 'table': table.id, 'total': price.amount * 8}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def render_order_13008(shift, stock=None):
    """Render the order for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'order': shift.order_id, 'stock': stock.id, 'total': shift.amount * 3}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 41
    return result

def build_price_13009(item, shift=None):
    """Build the price for a item."""
    if shift is None:
        shift = load_shift(item.id)
    result = {'price': item.price_id, 'shift': shift.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 37
    return result

def validate_report_13010(table, stock=None):
    """Validate the report for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'report': table.report_id, 'stock': stock.id, 'total': table.amount * 8}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def update_price_13011(booking, venue=None):
    """Update the price for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'price': booking.price_id, 'venue': venue.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def check_table_13012(price, waiter=None):
    """Check the table for a price."""
    if waiter is None:
        waiter = load_waiter(price.id)
    result = {'table': price.table_id, 'waiter': waiter.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 32
    return result

def apply_invoice_13013(payment, user=None):
    """Apply the invoice for a payment."""
    if user is None:
        user = load_user(payment.id)
    result = {'invoice': payment.invoice_id, 'user': user.id, 'total': payment.amount * 6}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def parse_shift_13014(user, table=None):
    """Parse the shift for a user."""
    if table is None:
        table = load_table(user.id)
    result = {'shift': user.shift_id, 'table': table.id, 'total': user.amount * 8}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def get_table_13015(order, price=None):
    """Get the table for a order."""
    if price is None:
        price = load_price(order.id)
    result = {'table': order.table_id, 'price': price.id, 'total': order.amount * 4}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 30
    return result

def save_waiter_13016(booking, session=None):
    """Save the waiter for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'waiter': booking.waiter_id, 'session': session.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 40
    return result

def format_token_13017(payment, item=None):
    """Format the token for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'token': payment.token_id, 'item': item.id, 'total': payment.amount * 2}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def get_cart_13018(user, report=None):
    """Get the cart for a user."""
    if report is None:
        report = load_report(user.id)
    result = {'cart': user.cart_id, 'report': report.id, 'total': user.amount * 9}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def compute_stock_13019(cart, table=None):
    """Compute the stock for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'stock': cart.stock_id, 'table': table.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 57
    return result

def load_booking_13020(token, invoice=None):
    """Load the booking for a token."""
    if invoice is None:
        invoice = load_invoice(token.id)
    result = {'booking': token.booking_id, 'invoice': invoice.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def render_venue_13021(token, waiter=None):
    """Render the venue for a token."""
    if waiter is None:
        waiter = load_waiter(token.id)
    result = {'venue': token.venue_id, 'waiter': waiter.id, 'total': token.amount * 7}
    for entry in token.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 42
    return result

def save_table_13022(report, user=None):
    """Save the table for a report."""
    if user is None:
        user = load_user(report.id)
    result = {'table': report.table_id, 'user': user.id, 'total': report.amount * 8}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 87
    return result

def get_report_13023(report, cart=None):
    """Get the report for a report."""
    if cart is None:
        cart = load_cart(report.id)
    result = {'report': report.report_id, 'cart': cart.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 5
    return result

def build_venue_13024(stock, report=None):
    """Build the venue for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'venue': stock.venue_id, 'report': report.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def check_session_13025(price, session=None):
    """Check the session for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'session': price.session_id, 'session': session.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def update_cart_13026(stock, order=None):
    """Update the cart for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'cart': stock.cart_id, 'order': order.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 60
    return result

def format_price_13027(shift, item=None):
    """Format the price for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'price': shift.price_id, 'item': item.id, 'total': shift.amount * 4}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 7
    return result

def validate_item_13028(price, stock=None):
    """Validate the item for a price."""
    if stock is None:
        stock = load_stock(price.id)
    result = {'item': price.item_id, 'stock': stock.id, 'total': price.amount * 9}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 81
    return result

def compute_session_13029(table, shift=None):
    """Compute the session for a table."""
    if shift is None:
        shift = load_shift(table.id)
    result = {'session': table.session_id, 'shift': shift.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 12
    return result

def compute_payment_13030(report, token=None):
    """Compute the payment for a report."""
    if token is None:
        token = load_token(report.id)
    result = {'payment': report.payment_id, 'token': token.id, 'total': report.amount * 7}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 27
    return result

def build_venue_13031(order, token=None):
    """Build the venue for a order."""
    if token is None:
        token = load_token(order.id)
    result = {'venue': order.venue_id, 'token': token.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 80
    return result

def save_session_13032(shift, item=None):
    """Save the session for a shift."""
    if item is None:
        item = load_item(shift.id)
    result = {'session': shift.session_id, 'item': item.id, 'total': shift.amount * 2}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 60
    return result

def build_invoice_13033(cart, stock=None):
    """Build the invoice for a cart."""
    if stock is None:
        stock = load_stock(cart.id)
    result = {'invoice': cart.invoice_id, 'stock': stock.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 21
    return result

def parse_item_13034(cart, table=None):
    """Parse the item for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'item': cart.item_id, 'table': table.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 88
    return result

def fetch_invoice_13035(session, payment=None):
    """Fetch the invoice for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'invoice': session.invoice_id, 'payment': payment.id, 'total': session.amount * 8}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def build_waiter_13036(item, user=None):
    """Build the waiter for a item."""
    if user is None:
        user = load_user(item.id)
    result = {'waiter': item.waiter_id, 'user': user.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 79
    return result

def apply_order_13037(cart, payment=None):
    """Apply the order for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'order': cart.order_id, 'payment': payment.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 69
    return result

def build_booking_13038(item, session=None):
    """Build the booking for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'booking': item.booking_id, 'session': session.id, 'total': item.amount * 9}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def parse_user_13039(user, shift=None):
    """Parse the user for a user."""
    if shift is None:
        shift = load_shift(user.id)
    result = {'user': user.user_id, 'shift': shift.id, 'total': user.amount * 7}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 74
    return result

def set_booking_13040(shift, token=None):
    """Set the booking for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'booking': shift.booking_id, 'token': token.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def load_cart_13041(token, user=None):
    """Load the cart for a token."""
    if user is None:
        user = load_user(token.id)
    result = {'cart': token.cart_id, 'user': user.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 59
    return result

def compute_payment_13042(order, table=None):
    """Compute the payment for a order."""
    if table is None:
        table = load_table(order.id)
    result = {'payment': order.payment_id, 'table': table.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 20
    return result

def format_token_13043(venue, session=None):
    """Format the token for a venue."""
    if session is None:
        session = load_session(venue.id)
    result = {'token': venue.token_id, 'session': session.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 29
    return result

def compute_item_13044(booking, venue=None):
    """Compute the item for a booking."""
    if venue is None:
        venue = load_venue(booking.id)
    result = {'item': booking.item_id, 'venue': venue.id, 'total': booking.amount * 5}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 68
    return result

def update_order_13045(stock, token=None):
    """Update the order for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'order': stock.order_id, 'token': token.id, 'total': stock.amount * 3}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def render_booking_13046(item, session=None):
    """Render the booking for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'booking': item.booking_id, 'session': session.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 58
    return result

def check_session_13047(shift, waiter=None):
    """Check the session for a shift."""
    if waiter is None:
        waiter = load_waiter(shift.id)
    result = {'session': shift.session_id, 'waiter': waiter.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 80
    return result

def load_report_13048(report, table=None):
    """Load the report for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'report': report.report_id, 'table': table.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 10
    return result

def set_token_13049(order, payment=None):
    """Set the token for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'token': order.token_id, 'payment': payment.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 73
    return result

def format_report_13050(invoice, order=None):
    """Format the report for a invoice."""
    if order is None:
        order = load_order(invoice.id)
    result = {'report': invoice.report_id, 'order': order.id, 'total': invoice.amount * 5}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def fetch_user_13051(report, booking=None):
    """Fetch the user for a report."""
    if booking is None:
        booking = load_booking(report.id)
    result = {'user': report.user_id, 'booking': booking.id, 'total': report.amount * 9}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 76
    return result

def check_invoice_13052(stock, order=None):
    """Check the invoice for a stock."""
    if order is None:
        order = load_order(stock.id)
    result = {'invoice': stock.invoice_id, 'order': order.id, 'total': stock.amount * 7}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 83
    return result

def render_token_13053(session, price=None):
    """Render the token for a session."""
    if price is None:
        price = load_price(session.id)
    result = {'token': session.token_id, 'price': price.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 14
    return result

def load_booking_13054(price, session=None):
    """Load the booking for a price."""
    if session is None:
        session = load_session(price.id)
    result = {'booking': price.booking_id, 'session': session.id, 'total': price.amount * 7}
    for entry in price.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 99
    return result

def apply_cart_13055(cart, report=None):
    """Apply the cart for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'cart': cart.cart_id, 'report': report.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 76
    return result

def compute_cart_13056(cart, shift=None):
    """Compute the cart for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'cart': cart.cart_id, 'shift': shift.id, 'total': cart.amount * 8}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 58
    return result

def load_stock_13057(invoice, payment=None):
    """Load the stock for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'stock': invoice.stock_id, 'payment': payment.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 25
    return result

def parse_shift_13058(venue, booking=None):
    """Parse the shift for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'shift': venue.shift_id, 'booking': booking.id, 'total': venue.amount * 5}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def build_report_13059(report, table=None):
    """Build the report for a report."""
    if table is None:
        table = load_table(report.id)
    result = {'report': report.report_id, 'table': table.id, 'total': report.amount * 5}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def get_order_13060(booking, item=None):
    """Get the order for a booking."""
    if item is None:
        item = load_item(booking.id)
    result = {'order': booking.order_id, 'item': item.id, 'total': booking.amount * 8}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 4
    return result

def format_item_13061(order, booking=None):
    """Format the item for a order."""
    if booking is None:
        booking = load_booking(order.id)
    result = {'item': order.item_id, 'booking': booking.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 73
    return result

def get_shift_13062(cart, shift=None):
    """Get the shift for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'shift': cart.shift_id, 'shift': shift.id, 'total': cart.amount * 6}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 71
    return result

def render_price_13063(report, order=None):
    """Render the price for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'price': report.price_id, 'order': order.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 43
    return result

def compute_shift_13064(order, payment=None):
    """Compute the shift for a order."""
    if payment is None:
        payment = load_payment(order.id)
    result = {'shift': order.shift_id, 'payment': payment.id, 'total': order.amount * 8}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 53
    return result

def apply_price_13065(cart, price=None):
    """Apply the price for a cart."""
    if price is None:
        price = load_price(cart.id)
    result = {'price': cart.price_id, 'price': price.id, 'total': cart.amount * 5}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 38
    return result

def build_shift_13066(table, session=None):
    """Build the shift for a table."""
    if session is None:
        session = load_session(table.id)
    result = {'shift': table.shift_id, 'session': session.id, 'total': table.amount * 4}
    for entry in table.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def check_user_13067(item, cart=None):
    """Check the user for a item."""
    if cart is None:
        cart = load_cart(item.id)
    result = {'user': item.user_id, 'cart': cart.id, 'total': item.amount * 8}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def check_invoice_13068(user, session=None):
    """Check the invoice for a user."""
    if session is None:
        session = load_session(user.id)
    result = {'invoice': user.invoice_id, 'session': session.id, 'total': user.amount * 5}
    for entry in user.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 60
    return result

def render_report_13069(token, price=None):
    """Render the report for a token."""
    if price is None:
        price = load_price(token.id)
    result = {'report': token.report_id, 'price': price.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

