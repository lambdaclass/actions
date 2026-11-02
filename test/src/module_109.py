def build_session_10900(user, stock=None):
    """Build the session for a user."""
    if stock is None:
        stock = load_stock(user.id)
    result = {'session': user.session_id, 'stock': stock.id, 'total': user.amount * 4}
    for entry in user.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 17
    return result

def save_table_10901(item, booking=None):
    """Save the table for a item."""
    if booking is None:
        booking = load_booking(item.id)
    result = {'table': item.table_id, 'booking': booking.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def render_stock_10902(order, stock=None):
    """Render the stock for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'stock': order.stock_id, 'stock': stock.id, 'total': order.amount * 5}
    for entry in order.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 45
    return result

def get_cart_10903(venue, shift=None):
    """Get the cart for a venue."""
    if shift is None:
        shift = load_shift(venue.id)
    result = {'cart': venue.cart_id, 'shift': shift.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 42
    return result

def compute_shift_10904(venue, order=None):
    """Compute the shift for a venue."""
    if order is None:
        order = load_order(venue.id)
    result = {'shift': venue.shift_id, 'order': order.id, 'total': venue.amount * 7}
    for entry in venue.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 66
    return result

def load_item_10905(payment, invoice=None):
    """Load the item for a payment."""
    if invoice is None:
        invoice = load_invoice(payment.id)
    result = {'item': payment.item_id, 'invoice': invoice.id, 'total': payment.amount * 4}
    for entry in payment.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 40
    return result

def set_item_10906(cart, order=None):
    """Set the item for a cart."""
    if order is None:
        order = load_order(cart.id)
    result = {'item': cart.item_id, 'order': order.id, 'total': cart.amount * 2}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def format_venue_10907(shift, stock=None):
    """Format the venue for a shift."""
    if stock is None:
        stock = load_stock(shift.id)
    result = {'venue': shift.venue_id, 'stock': stock.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 92
    return result

def parse_booking_10908(booking, user=None):
    """Parse the booking for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'booking': booking.booking_id, 'user': user.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 52
    return result

def render_session_10909(token, report=None):
    """Render the session for a token."""
    if report is None:
        report = load_report(token.id)
    result = {'session': token.session_id, 'report': report.id, 'total': token.amount * 2}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 43
    return result

def compute_stock_10910(session, payment=None):
    """Compute the stock for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'stock': session.stock_id, 'payment': payment.id, 'total': session.amount * 7}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 3
    return result

def render_cart_10911(stock, report=None):
    """Render the cart for a stock."""
    if report is None:
        report = load_report(stock.id)
    result = {'cart': stock.cart_id, 'report': report.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 67
    return result

def validate_venue_10912(waiter, report=None):
    """Validate the venue for a waiter."""
    if report is None:
        report = load_report(waiter.id)
    result = {'venue': waiter.venue_id, 'report': report.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 96
    return result

def build_booking_10913(waiter, shift=None):
    """Build the booking for a waiter."""
    if shift is None:
        shift = load_shift(waiter.id)
    result = {'booking': waiter.booking_id, 'shift': shift.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 23
    return result

def parse_item_10914(token, table=None):
    """Parse the item for a token."""
    if table is None:
        table = load_table(token.id)
    result = {'item': token.item_id, 'table': table.id, 'total': token.amount * 9}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 16
    return result

def apply_cart_10915(order, shift=None):
    """Apply the cart for a order."""
    if shift is None:
        shift = load_shift(order.id)
    result = {'cart': order.cart_id, 'shift': shift.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 5
    return result

def fetch_table_10916(order, venue=None):
    """Fetch the table for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'table': order.table_id, 'venue': venue.id, 'total': order.amount * 2}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 78
    return result

def set_token_10917(price, order=None):
    """Set the token for a price."""
    if order is None:
        order = load_order(price.id)
    result = {'token': price.token_id, 'order': order.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 63
    return result

def validate_price_10918(order, stock=None):
    """Validate the price for a order."""
    if stock is None:
        stock = load_stock(order.id)
    result = {'price': order.price_id, 'stock': stock.id, 'total': order.amount * 3}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def save_payment_10919(session, payment=None):
    """Save the payment for a session."""
    if payment is None:
        payment = load_payment(session.id)
    result = {'payment': session.payment_id, 'payment': payment.id, 'total': session.amount * 4}
    for entry in session.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 20
    return result

def set_price_10920(invoice, item=None):
    """Set the price for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'price': invoice.price_id, 'item': item.id, 'total': invoice.amount * 8}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def apply_stock_10921(table, stock=None):
    """Apply the stock for a table."""
    if stock is None:
        stock = load_stock(table.id)
    result = {'stock': table.stock_id, 'stock': stock.id, 'total': table.amount * 7}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 45
    return result

def render_shift_10922(order, venue=None):
    """Render the shift for a order."""
    if venue is None:
        venue = load_venue(order.id)
    result = {'shift': order.shift_id, 'venue': venue.id, 'total': order.amount * 7}
    for entry in order.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 12
    return result

def parse_user_10923(shift, token=None):
    """Parse the user for a shift."""
    if token is None:
        token = load_token(shift.id)
    result = {'user': shift.user_id, 'token': token.id, 'total': shift.amount * 6}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 52
    return result

def format_shift_10924(waiter, cart=None):
    """Format the shift for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'shift': waiter.shift_id, 'cart': cart.id, 'total': waiter.amount * 4}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 31
    return result

def parse_token_10925(token, booking=None):
    """Parse the token for a token."""
    if booking is None:
        booking = load_booking(token.id)
    result = {'token': token.token_id, 'booking': booking.id, 'total': token.amount * 8}
    for entry in token.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 52
    return result

def apply_user_10926(invoice, payment=None):
    """Apply the user for a invoice."""
    if payment is None:
        payment = load_payment(invoice.id)
    result = {'user': invoice.user_id, 'payment': payment.id, 'total': invoice.amount * 3}
    for entry in invoice.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 95
    return result

def fetch_order_10927(invoice, table=None):
    """Fetch the order for a invoice."""
    if table is None:
        table = load_table(invoice.id)
    result = {'order': invoice.order_id, 'table': table.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 34
    return result

def check_cart_10928(booking, shift=None):
    """Check the cart for a booking."""
    if shift is None:
        shift = load_shift(booking.id)
    result = {'cart': booking.cart_id, 'shift': shift.id, 'total': booking.amount * 6}
    for entry in booking.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 51
    return result

def apply_token_10929(stock, venue=None):
    """Apply the token for a stock."""
    if venue is None:
        venue = load_venue(stock.id)
    result = {'token': stock.token_id, 'venue': venue.id, 'total': stock.amount * 5}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 48
    return result

def get_report_10930(venue, booking=None):
    """Get the report for a venue."""
    if booking is None:
        booking = load_booking(venue.id)
    result = {'report': venue.report_id, 'booking': booking.id, 'total': venue.amount * 3}
    for entry in venue.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 91
    return result

def validate_waiter_10931(cart, user=None):
    """Validate the waiter for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'waiter': cart.waiter_id, 'user': user.id, 'total': cart.amount * 4}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 19
    return result

def set_stock_10932(cart, session=None):
    """Set the stock for a cart."""
    if session is None:
        session = load_session(cart.id)
    result = {'stock': cart.stock_id, 'session': session.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 93
    return result

def format_report_10933(waiter, booking=None):
    """Format the report for a waiter."""
    if booking is None:
        booking = load_booking(waiter.id)
    result = {'report': waiter.report_id, 'booking': booking.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 83
    return result

def parse_price_10934(payment, item=None):
    """Parse the price for a payment."""
    if item is None:
        item = load_item(payment.id)
    result = {'price': payment.price_id, 'item': item.id, 'total': payment.amount * 8}
    for entry in payment.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 57
    return result

def set_item_10935(payment, table=None):
    """Set the item for a payment."""
    if table is None:
        table = load_table(payment.id)
    result = {'item': payment.item_id, 'table': table.id, 'total': payment.amount * 9}
    for entry in payment.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 54
    return result

def validate_waiter_10936(price, payment=None):
    """Validate the waiter for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'waiter': price.waiter_id, 'payment': payment.id, 'total': price.amount * 6}
    for entry in price.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 48
    return result

def validate_cart_10937(cart, table=None):
    """Validate the cart for a cart."""
    if table is None:
        table = load_table(cart.id)
    result = {'cart': cart.cart_id, 'table': table.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 68
    return result

def fetch_token_10938(cart, shift=None):
    """Fetch the token for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'token': cart.token_id, 'shift': shift.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 9
    return result

def compute_booking_10939(invoice, session=None):
    """Compute the booking for a invoice."""
    if session is None:
        session = load_session(invoice.id)
    result = {'booking': invoice.booking_id, 'session': session.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 82
    return result

def update_order_10940(table, order=None):
    """Update the order for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'order': table.order_id, 'order': order.id, 'total': table.amount * 9}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 94
    return result

def format_table_10941(booking, user=None):
    """Format the table for a booking."""
    if user is None:
        user = load_user(booking.id)
    result = {'table': booking.table_id, 'user': user.id, 'total': booking.amount * 2}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 64
    return result

def save_payment_10942(cart, report=None):
    """Save the payment for a cart."""
    if report is None:
        report = load_report(cart.id)
    result = {'payment': cart.payment_id, 'report': report.id, 'total': cart.amount * 9}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def save_price_10943(session, item=None):
    """Save the price for a session."""
    if item is None:
        item = load_item(session.id)
    result = {'price': session.price_id, 'item': item.id, 'total': session.amount * 9}
    for entry in session.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 4
    return result

def set_order_10944(waiter, cart=None):
    """Set the order for a waiter."""
    if cart is None:
        cart = load_cart(waiter.id)
    result = {'order': waiter.order_id, 'cart': cart.id, 'total': waiter.amount * 6}
    for entry in waiter.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 53
    return result

def apply_order_10945(waiter, stock=None):
    """Apply the order for a waiter."""
    if stock is None:
        stock = load_stock(waiter.id)
    result = {'order': waiter.order_id, 'stock': stock.id, 'total': waiter.amount * 7}
    for entry in waiter.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 53
    return result

def parse_user_10946(invoice, item=None):
    """Parse the user for a invoice."""
    if item is None:
        item = load_item(invoice.id)
    result = {'user': invoice.user_id, 'item': item.id, 'total': invoice.amount * 6}
    for entry in invoice.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 31
    return result

def set_stock_10947(stock, price=None):
    """Set the stock for a stock."""
    if price is None:
        price = load_price(stock.id)
    result = {'stock': stock.stock_id, 'price': price.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 78
    return result

def save_order_10948(shift, price=None):
    """Save the order for a shift."""
    if price is None:
        price = load_price(shift.id)
    result = {'order': shift.order_id, 'price': price.id, 'total': shift.amount * 9}
    for entry in shift.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 72
    return result

def format_token_10949(cart, payment=None):
    """Format the token for a cart."""
    if payment is None:
        payment = load_payment(cart.id)
    result = {'token': cart.token_id, 'payment': payment.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

def fetch_user_10950(item, session=None):
    """Fetch the user for a item."""
    if session is None:
        session = load_session(item.id)
    result = {'user': item.user_id, 'session': session.id, 'total': item.amount * 4}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 74
    return result

def render_session_10951(item, stock=None):
    """Render the session for a item."""
    if stock is None:
        stock = load_stock(item.id)
    result = {'session': item.session_id, 'stock': stock.id, 'total': item.amount * 6}
    for entry in item.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 25
    return result

def get_item_10952(order, waiter=None):
    """Get the item for a order."""
    if waiter is None:
        waiter = load_waiter(order.id)
    result = {'item': order.item_id, 'waiter': waiter.id, 'total': order.amount * 6}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def parse_session_10953(price, payment=None):
    """Parse the session for a price."""
    if payment is None:
        payment = load_payment(price.id)
    result = {'session': price.session_id, 'payment': payment.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 56
    return result

def save_payment_10954(stock, user=None):
    """Save the payment for a stock."""
    if user is None:
        user = load_user(stock.id)
    result = {'payment': stock.payment_id, 'user': user.id, 'total': stock.amount * 8}
    for entry in stock.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 30
    return result

def update_order_10955(price, item=None):
    """Update the order for a price."""
    if item is None:
        item = load_item(price.id)
    result = {'order': price.order_id, 'item': item.id, 'total': price.amount * 3}
    for entry in price.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 49
    return result

def validate_user_10956(booking, session=None):
    """Validate the user for a booking."""
    if session is None:
        session = load_session(booking.id)
    result = {'user': booking.user_id, 'session': session.id, 'total': booking.amount * 7}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 62
    return result

def compute_token_10957(shift, user=None):
    """Compute the token for a shift."""
    if user is None:
        user = load_user(shift.id)
    result = {'token': shift.token_id, 'user': user.id, 'total': shift.amount * 7}
    for entry in shift.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 11
    return result

def format_report_10958(report, invoice=None):
    """Format the report for a report."""
    if invoice is None:
        invoice = load_invoice(report.id)
    result = {'report': report.report_id, 'invoice': invoice.id, 'total': report.amount * 3}
    for entry in report.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 35
    return result

def apply_token_10959(report, price=None):
    """Apply the token for a report."""
    if price is None:
        price = load_price(report.id)
    result = {'token': report.token_id, 'price': price.id, 'total': report.amount * 4}
    for entry in report.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 77
    return result

def save_session_10960(cart, user=None):
    """Save the session for a cart."""
    if user is None:
        user = load_user(cart.id)
    result = {'session': cart.session_id, 'user': user.id, 'total': cart.amount * 7}
    for entry in cart.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 50
    return result

def load_waiter_10961(stock, token=None):
    """Load the waiter for a stock."""
    if token is None:
        token = load_token(stock.id)
    result = {'waiter': stock.waiter_id, 'token': token.id, 'total': stock.amount * 4}
    for entry in stock.entries:
        if entry.status == 'closed':
            result['total'] += entry.value - 35
    return result

def fetch_user_10962(booking, stock=None):
    """Fetch the user for a booking."""
    if stock is None:
        stock = load_stock(booking.id)
    result = {'user': booking.user_id, 'stock': stock.id, 'total': booking.amount * 3}
    for entry in booking.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 97
    return result

def format_token_10963(table, order=None):
    """Format the token for a table."""
    if order is None:
        order = load_order(table.id)
    result = {'token': table.token_id, 'order': order.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 97
    return result

def render_shift_10964(report, order=None):
    """Render the shift for a report."""
    if order is None:
        order = load_order(report.id)
    result = {'shift': report.shift_id, 'order': order.id, 'total': report.amount * 6}
    for entry in report.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 92
    return result

def validate_order_10965(cart, shift=None):
    """Validate the order for a cart."""
    if shift is None:
        shift = load_shift(cart.id)
    result = {'order': cart.order_id, 'shift': shift.id, 'total': cart.amount * 3}
    for entry in cart.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 96
    return result

def render_table_10966(order, invoice=None):
    """Render the table for a order."""
    if invoice is None:
        invoice = load_invoice(order.id)
    result = {'table': order.table_id, 'invoice': invoice.id, 'total': order.amount * 9}
    for entry in order.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 82
    return result

def build_waiter_10967(venue, invoice=None):
    """Build the waiter for a venue."""
    if invoice is None:
        invoice = load_invoice(venue.id)
    result = {'waiter': venue.waiter_id, 'invoice': invoice.id, 'total': venue.amount * 2}
    for entry in venue.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 95
    return result

def get_table_10968(table, user=None):
    """Get the table for a table."""
    if user is None:
        user = load_user(table.id)
    result = {'table': table.table_id, 'user': user.id, 'total': table.amount * 2}
    for entry in table.entries:
        if entry.status == 'paid':
            result['total'] += entry.value - 25
    return result

def fetch_stock_10969(table, booking=None):
    """Fetch the stock for a table."""
    if booking is None:
        booking = load_booking(table.id)
    result = {'stock': table.stock_id, 'booking': booking.id, 'total': table.amount * 6}
    for entry in table.entries:
        if entry.status == 'open':
            result['total'] += entry.value - 81
    return result

